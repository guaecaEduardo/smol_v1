


class RequirementClassifierAgent(ToolCallingAgent):
    async def step(self, state: AgentState):
        index = state.get("current_index", 0)
        if index >= len(state["requirements"]["rows"]):
            return state.set("done", True)

        requirement = state["requirements"]["rows"][index]

        if "C1feature" in requirement:
            state.set("current_index", index + 1)
            return state

        result = await self.tools["requirement_classifier"].call(requirement["description"])

        feature_id = result.get("feature_id")
        new_feature = result.get("new_feature")

        if feature_id or new_feature:
            await self.tools["feature_updater"].call(
                requirement["id"],
                feature_id,
                new_feature
            )

        state.set("current_index", index + 1)
        return state
