from agents import billing, general, technical



def triage(user_input, context):
    if "refund" in user_input.lower():
        context.issue_type = "billing"
        return billing.handle(context, user_input)
    elif "restart" in user_input.lower() or "service" in user_input.lower():
        context.issue_type = "technical"
        return technical.handle(context, user_input)
    else: 
        context.issue_type = "general"
        return general.handle(context, user_input)
    