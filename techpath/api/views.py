from django.shortcuts import render

# View for the survey page
def survey(request):
    return render(request, 'api/survey.html')

# View for the result page
def result(request):
    if request.method == 'POST':
        # interest_text = request.POST.get('interest') # Not used in logic, but good to have
        tools = request.POST.getlist('tools') # Gets a list of selected tools
        activity = request.POST.get('activity')

        tech_path = 'Undetermined'
        match_type = 'Soft' # Default to soft match
        badge_color = 'bg-warning' # Default to yellow badge

        # Rule-based logic
        if 'Unity' in tools and activity == 'building games':
            tech_path = 'Game Development'
            match_type = 'Confident'
            badge_color = 'bg-success'
        elif 'Unity' in tools :
             tech_path = 'Game Development'
             match_type = 'Soft'
             badge_color = 'bg-warning'
        elif activity == 'building games':
            tech_path = 'Game Development'
            match_type = 'Soft'
            badge_color = 'bg-warning'

        elif 'Python' in tools and activity == 'analyzing data':
            tech_path = 'Data Science'
            match_type = 'Confident'
            badge_color = 'bg-success'
        elif 'Python' in tools :
            tech_path = 'Data Science'
            match_type = 'Soft'
            badge_color = 'bg-warning'
        elif activity == 'analyzing data':
            tech_path = 'Data Science'
            match_type = 'Soft'
            badge_color = 'bg-warning'


        elif 'Terminal' in tools and activity == 'building websites':
            tech_path = 'Web Development'
            match_type = 'Confident'
            badge_color = 'bg-success'
        elif 'Terminal' in tools :
            tech_path = 'Web Development'
            match_type = 'Soft'
            badge_color = 'bg-warning'
        elif activity == 'building websites':
            tech_path = 'Web Development'
            match_type = 'Soft'
            badge_color = 'bg-warning'


        elif 'Excel' in tools and activity == 'securing systems': # This rule seems a bit odd, but following spec
            tech_path = 'Cybersecurity'
            match_type = 'Confident'
            badge_color = 'bg-success'
        elif 'Excel' in tools:
            tech_path = 'Data Analysis / Business Intelligence' # More common use of Excel
            match_type = 'Soft'
            badge_color = 'bg-warning'
        elif activity == 'securing systems':
             tech_path = 'Cybersecurity'
             match_type = 'Soft'
             badge_color = 'bg-warning'


        elif 'Figma' in tools and activity == 'designing UIs':
            tech_path = 'UI/UX Design'
            match_type = 'Confident'
            badge_color = 'bg-success'
        elif 'Figma' in tools:
            tech_path = 'UI/UX Design'
            match_type = 'Soft'
            badge_color = 'bg-warning'
        elif activity == 'designing UIs':
            tech_path = 'UI/UX Design'
            match_type = 'Soft'
            badge_color = 'bg-warning'

        # Fallback if no specific rules met but some selections made
        elif not tools and not activity:
            tech_path = 'Explore various tech fields!'
            match_type = 'General'
            badge_color = 'bg-info'
        elif tools or activity:
            if tech_path == 'Undetermined': # If no primary rule hit
                tech_path = 'General Tech Exploration'
                match_type = 'Soft'
                badge_color = 'bg-secondary'


        context = {
            'tech_path': tech_path,
            'match_type': match_type,
            'badge_color': badge_color,
        }
        return render(request, 'api/result.html', context)
    else:
        # If not POST, redirect to survey (though direct access to /result/ via GET shouldn't happen with current setup)
        return render(request, 'api/survey.html')
