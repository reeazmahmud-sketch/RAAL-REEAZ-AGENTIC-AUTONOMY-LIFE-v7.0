import unittest

from raal.executor import SimulatedExecutor
from raal.models import Goal
from raal.planner import DeterministicPlanner


class SimulatedExecutorTests(unittest.TestCase):
    def test_executor_records_expected_events(self) -> None:
        plan = DeterministicPlanner(max_steps=4).plan(Goal(title="Prepare demo"))
        executor = SimulatedExecutor()

        result = executor.run(plan)

        self.assertEqual(result.status, "simulated_success")
        self.assertEqual(result.completed_steps, len(plan.steps))
        events = executor.audit_log.events
        self.assertEqual(events[0].kind, "execution.started")
        self.assertEqual(events[-1].kind, "execution.completed")
        simulated_steps = [event for event in events if event.kind == "execution.step.simulated"]
        self.assertEqual(len(simulated_steps), len(plan.steps))


if __name__ == "__main__":
    unittest.main()
