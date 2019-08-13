rule "Between 0 and 6 o'clock""
when
    to_date($message.timestamp).hourOfDay >=0 &&
    to_date($message.timestamp).hourOfDay =<6
then
    set_field("trigger_alert", true)
end