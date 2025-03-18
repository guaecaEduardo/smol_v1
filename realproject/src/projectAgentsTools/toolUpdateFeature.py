# FIX APPLIED:
# from agentsTools.shared import Tool

# FIX APPLIED:
# from some_module import Tool

class FeatureUpdateTool(Tool):
    def __init__(self, feature_file, requirement_file):
        super().__init__(name="feature_updater", description="Update feature list and requirements.")
        self.feature_file = feature_file
        self.requirement_file = requirement_file
    
    async def call(self, requirement_id, feature_id, new_feature=None):
        with open(self.feature_file, "r", encoding="utf-8") as f:
            features = json.load(f)

        if new_feature:
            new_id = f"C1F_{len(features) + 1}"
            features[new_id] = {
                "name": new_feature["name"],
                "description": new_feature["description"]
            }
            feature_id = new_id

            with open(self.feature_file, "w", encoding="utf-8") as f:
                json.dump(features, f, indent=2)

        # Update the requirement
        with open(self.requirement_file, "r", encoding="utf-8") as f:
            requirements = json.load(f)

        for req in requirements["rows"]:
            if req["id"] == requirement_id:
                req["C1feature"] = feature_id

        with open(self.requirement_file, "w", encoding="utf-8") as f:
            json.dump(requirements, f, indent=2)

        return {"status": "success", "feature_id": feature_id}
