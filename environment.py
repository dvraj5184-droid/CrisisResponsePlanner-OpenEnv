import numpy as np
import random

class CrisisResponseEnv:
    def __init__(self, difficulty='medium'):
        self.difficulty = difficulty
        self.reset()

    def reset(self):
        random.seed(42)
        self.state_data = {
            "infrastructure": {
                "power_grid": 100,      # Impacted by floods
                "road_network": 1.0,    # 1.0 = Clear, 0.0 = Blocked
                "hospital_load": 20     # Percentage
            },
            "zones": {
                "Zone_1": {"type": "Urban", "risk": 0.1, "population": 5000, "status": "Stable"},
                "Zone_2": {"type": "Industrial", "risk": 0.4, "population": 2000, "status": "Warning"}
            },
            "inventory": {"medics": 10, "engineers": 10, "drones": 5},
            "step": 0
        }
        return self.state()

    def state(self):
        return {
            "observation": self.state_data,
            "reward": self.calculate_reward(),
            "done": self.state_data["step"] >= 20
        }

    def step(self, action):
        # Action format: {"zone": "Zone_1", "dispatch": "engineers"}
        zone = action.get("zone")
        unit = action.get("dispatch")

        # 1. Dynamic State Transition & Cascading Failure
        if self.state_data["infrastructure"]["power_grid"] < 50:
            self.state_data["infrastructure"]["hospital_load"] += 10 # Power loss slows hospitals
        
        # 2. Uncertainty Modeling (Hazard Growth)
        for z in self.state_data["zones"].values():
            z["risk"] = min(1.0, z["risk"] + random.uniform(0.02, 0.08))

        # 3. Decision Logic
        if unit in self.state_data["inventory"] and self.state_data["inventory"][unit] > 0:
            self.state_data["inventory"][unit] -= 1
            self.state_data["zones"][zone]["risk"] *= 0.5 # Unit reduces risk
        
        self.state_data["step"] += 1
        return self.state()

    def calculate_reward(self):
        # Case 4: Non-binary Continuous Reward
        avg_risk = sum(z["risk"] for z in self.state_data["zones"].values()) / 2
        stability = self.state_data["infrastructure"]["power_grid"] / 100
        return round(1.0 - (0.7 * avg_risk) - (0.3 * (1 - stability)), 4)
