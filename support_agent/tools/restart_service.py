def restart_service(context):
    if context.issue_type == "technical":
        return "Your services has been restarted successfully."
    return "Restart is only available for technical issues."
