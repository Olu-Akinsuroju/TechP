from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def suggest_path(request):
    data = request.data
    # interest_reason = data.get('interestReason', '') # Not used in logic but was in Flask
    tools = data.get("tools", [])
    activity = data.get("activity")

    path = "General Tech" # Default path
    reason = "Based on your interests, a general tech path might be suitable." # Default reason

    if activity == "analyzing data":
        path = "Data Science"
        reason = "You're excited about analyzing data, which is a core part of Data Science."
    elif activity == "building websites" and "Terminal" in tools:
        path = "Web Development"
        reason = "You're interested in building websites and are comfortable with the Terminal, a key combination for Web Development."
    elif activity == "building websites":
        path = "Web Development (Frontend Focus)"
        reason = "You're interested in building websites. Focusing on frontend technologies could be a good start."
    elif "Unity" in tools and activity == "building games":
        path = "Game Development"
        reason = "Your comfort with Unity and excitement for building games points directly to Game Development."
    elif "Unity" in tools: # Broader Unity case
        path = "Game Development or AR/VR Development"
        reason = "Your comfort with Unity opens doors to Game Development or AR/VR fields."
    elif activity == "building games": # General game interest
        path = "Game Development"
        reason = "You're excited about building games. Exploring game engines and programming would be next steps."
    elif activity == "securing systems":
        path = "Cybersecurity"
        reason = "Your interest in securing systems is key for a Cybersecurity path."
    elif activity == "designing UIs":
        path = "UI/UX Design"
        reason = "Excitement about designing UIs is central to UI/UX Design."
    # Add other rules as needed

    return Response({"techPath": path, "reason": reason})
