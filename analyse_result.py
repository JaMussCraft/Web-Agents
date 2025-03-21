from agentlab.analyze import inspect_results

from browsergym.experiments.loop import (
    AbstractAgentArgs,
    EnvArgs,
    ExpArgs,
    ExpResult,
    StepInfo,
    StepTimestamps,
)

# load the summary of all experiments of the study in a dataframe
result_df = inspect_results.load_result_df("experiment-results/2025-03-20_15-54-25_genericagent-gpt-4o-mini-2024-07-18-on-miniwob-tiny-test")

# load the detailed results of the 1st experiment
exp_result = ExpResult(result_df["exp_dir"][0])
step_0_screenshot = exp_result.screenshots[0]
step_0_action = exp_result.steps_info[0].action
print(step_0_screenshot)
print(step_0_action)