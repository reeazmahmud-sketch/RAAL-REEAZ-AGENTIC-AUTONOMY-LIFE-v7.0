import unittest

from raal.models import Goal
from raal.planner import DeterministicPlanner


class DeterministicPlannerTests(unittest.TestCase):
    def test_plan_is_deterministic_for_same_input(self) -> None:
        planner = DeterministicPlanner(max_steps=6)
        goal = Goal(title="  Build a weekly study plan  ", context=" Focus on Python and math. ")

        first = planner.plan(goal)
        second = planner.plan(goal)

        self.assertEqual(first, second)
        self.assertEqual(first.goal.title, "Build a weekly study plan")
        self.assertEqual(first.goal.context, "Focus on Python and math.")

    def test_plan_respects_max_steps(self) -> None:
        planner = DeterministicPlanner(max_steps=3)
        plan = planner.plan(Goal(title="Test"))

        self.assertEqual(len(plan.steps), 3)
        self.assertEqual(plan.steps[0].index, 1)
        self.assertEqual(plan.steps[-1].index, 3)


if __name__ == "__main__":
    unittest.main()
