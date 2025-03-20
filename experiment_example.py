# Import your agent configuration extending bgym.AgentArgs class
# Make sure this object is imported from a module accessible in PYTHONPATH to properly unpickle
from agentlab.agents.generic_agent import AGENT_4o_MINI 

from agentlab.experiments.study import make_study

print(AGENT_4o_MINI)

study = make_study(
    benchmark="miniwob",  # or "webarena", "workarena_l1" ...
    agent_args=[AGENT_4o_MINI],
    comment="My first study",
)

study.run(n_jobs=5)