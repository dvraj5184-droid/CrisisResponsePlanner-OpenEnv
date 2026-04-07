import gradio as gr

def mission_control_run(task_type):
    # This simulates the 'Mission Control' Dashboard visual behavior
    return {
        "Risk Heatmap": "Updates...",
        "Resource Load": "Medics: 80% | Engineers: 40%",
        "Decision Log": f"AI Agent initiating {task_type} response protocol."
    }

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🛰️ CrisisResponsePlanner-OpenEnv: Mission Control")
    
    with gr.Row():
        with gr.Column(scale=2):
            task_select = gr.Dropdown(["easy", "medium", "hard"], label="Select Operational Task")
            btn = gr.Button("Deploy AI Agent", variant="primary")
        with gr.Column(scale=1):
            reward_display = gr.Label(label="Live Reward Signal")

    with gr.Row():
        heatmap = gr.Textbox(label="Left Panel: Incident Map Engine")
        timeline = gr.Textbox(label="Center Panel: Decision Timeline")
        resources = gr.Textbox(label="Right Panel: Resource Status")

    btn.click(mission_control_run, inputs=[task_select], outputs=[timeline])

demo.launch()
