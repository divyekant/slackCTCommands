# All command Match Templates

trend_base_template_with_property3 = "Show me the (.*) of (.*) where (.*) in the last (.*) days with (.*) and (.*)"
trend_base_template_with_property4 = "Show me the (.*) for (.*) where (.*) in the last (.*) days with (.*) and (.*)"
trend_base_template_with_property5 = "Show me (.*) of (.*) where (.*) in the last (.*) days with (.*) and (.*)"
trend_base_template_with_property6 = "Show me (.*) for (.*) where (.*) in the last (.*) days with (.*) and (.*)"
trend_base_template_with_property7 = "Show (.*) of (.*) where (.*) in the last (.*) days with (.*) and (.*)"
trend_base_template_with_property8 = "Show (.*) for (.*) where (.*) in the last (.*) days with (.*) and (.*)"

trend_base_template_with_time3 = "Show me the (.*) of (.*) in the last (.*) days with (.*) and (.*)"
trend_base_template_with_time4 = "Show me the (.*) for (.*) in the last (.*) days with (.*) and (.*)"
trend_base_template_with_time5 = "Show me (.*) of (.*) in the last (.*) days with (.*) and (.*)"
trend_base_template_with_time6 = "Show me (.*) for (.*) in the last (.*) days with (.*) and (.*)"
trend_base_template_with_time7 = "Show (.*) of (.*) in the last (.*) days with (.*) and (.*)"
trend_base_template_with_time8 = "Show (.*) for (.*) in the last (.*) days with (.*) and (.*)"

trend_base_template3 = "Show me the (.*) of (.*) with (.*) and (.*)"
trend_base_template4 = "Show me the (.*) for (.*) with (.*) and (.*)"
trend_base_template5 = "Show me (.*) of (.*) with (.*) and (.*)"
trend_base_template6 = "Show me (.*) for (.*) with (.*) and (.*)"
trend_base_template7 = "Show (.*) of (.*) with (.*) and (.*)"
trend_base_template8 = "Show (.*) for (.*) with (.*) and (.*)"

command_templates = [trend_base_template_with_property3, trend_base_template_with_property4,
                     trend_base_template_with_property5, trend_base_template_with_property6,
                     trend_base_template_with_property7, trend_base_template_with_property8,
                     trend_base_template_with_time3,
                     trend_base_template_with_time4, trend_base_template_with_time5, trend_base_template_with_time6,
                     trend_base_template_with_time7, trend_base_template_with_time8, trend_base_template3,
                     trend_base_template4, trend_base_template5,
                     trend_base_template6, trend_base_template7, trend_base_template8]

# templatetoken constants
template_replacement_token = "(.*)"
trend_base_template_token_count = trend_base_template3.count(template_replacement_token)
trend_base_template_with_time_token_count = trend_base_template_with_time3.count(template_replacement_token)
trend_base_template_with_property_token_count = trend_base_template_with_property3.count(template_replacement_token)

# ERROR CODES
error_command_not_matched = "command_not_matched"
error_command_not_matched_message = "Oops! the command message does not follow the pattern. Please try /cleverbot help " \
                                    "to know exact commands "
error_API_keys_mismatch = "error_API_keys_mismatch"
error_API_keys_mismatch_message = "Oops! Mandatory keys not provided in the command. Please try /cleverbot help " \
                                  "to know exact commands "

# CommandTypes
trend = "trend"

# Command Keys
event_name = "event_name"
from_date = "from_date"
to_date = "to_date"
user_property_name = "user_property_name"
event_property_name = "event_property_name"
account_id = "account_id"
account_passcode = "account_passcode"
command_type = "command_type"
days = "days"

# Command Structure
trend_command_base_keys = [command_type, event_name, days, account_id, account_passcode]
trend_command_base_keys_with_time = [command_type, event_name, days, account_id, account_passcode]
trend_command_base_keys_with_property = [command_type, event_name, event_property_name, days, account_id,
                                         account_passcode]
# Styling
BLACK_COLOUR_HEX = '#000000'
WHITE_COLOUR_HEX = '#ffffff'

# CT API Query Constants
default_lookback_days = 30
trendsAPI_mandatory_keys = [event_name, account_id, account_passcode]

# Charts defaults
chart_trend_style = {
    "fill": False,
    "borderColor": 'rgba(25, 108, 248, 1)'
}
