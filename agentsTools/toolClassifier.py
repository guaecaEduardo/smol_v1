from smolagents import Tool

class RequirementClassifierTool(Tool):
    def __init__(self, feature_file, context_file):
        super().__init__(name="requirement_classifier", description="Classify requirement into big features.")
        self.feature_file = feature_file
        self.context = load_project_context(context_file)

    async def call(self, requirement):
        with open(self.feature_file, "r", encoding="utf-8") as f:
            features = json.load(f)

        feature_list = "\n".join(
            [f"{k}: {v['name']} - {v['description']}" for k, v in features.items()]
        )

        # Add project context to the prompt
        prompt = (
            f"Project Context:\n"
            f"Project Name: {self.context['project_name']}\n"
            f"Goal: {self.context['project_goal']}\n"
            f"Target Users: {self.context['target_users']}\n"
            f"Platform: {self.context['platform']}\n\n"
            f"Classify the following requirement:\n"
            f"{requirement}\n\n"
            f"Available Features:\n{feature_list}\n\n"
            f"If none of these fit, propose a new feature with a name and description."
        )

        response = await self.model(prompt)
        result_text = response.get("choices", [{}])[0].get("text", "").strip()

        if result_text in features.keys():
            return {"feature_id": result_text, "new_feature": None}
        else:
            try:
                new_feature, new_description = result_text.split(" - ", 1)
            except ValueError:
                new_feature = result_text
                new_description = "No description provided."
            
            return {
                "feature_id": None,
                "new_feature": {
                    "name": new_feature.strip(),
                    "description": new_description.strip()
                }
            }
