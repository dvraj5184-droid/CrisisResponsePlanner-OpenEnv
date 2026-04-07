class TaskSuite:
    def __init__(self, env):
        self.env = env

    def evaluate(self, task_id):
        report = {"score": 0.0, "reward": 0.0, "feedback": ""}
        
        if task_id == "easy":
            # Rule: Score is high if risk in Zone_1 is below 30%
            report["score"] = 1.0 if self.env.state_data["zones"]["Zone_1"]["risk"] < 0.3 else 0.5
            report["feedback"] = "Urban stabilization achieved."
        
        elif task_id == "medium":
            # Rule: Balance resource usage vs risk reduction
            report["score"] = self.env.calculate_reward()
            report["feedback"] = "Multi-zone coordination analyzed."
            
        elif task_id == "hard":
            # Rule: Fail if power grid collapses
            report["score"] = 0.0 if self.env.state_data["infrastructure"]["power_grid"] < 10 else 0.9
            report["feedback"] = "Cascading failure prevention status: Critical."
            
        return report
