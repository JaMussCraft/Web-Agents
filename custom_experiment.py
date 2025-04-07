from browsergym.experiment.loop import ExpArgs

exp_args = ExpArgs(
    agent_args=CustomAgentArgs(custom_param="value"),
    env_args=env_args,
    exp_dir="./experiments",
    exp_name="custom_experiment",
    enable_debug=True,
)

# Run the experiment
exp_args.prepare()
exp_args.run()