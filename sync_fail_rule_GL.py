rule "alert_on_sync_failures"
when
    has_field("sync_node") AND
    to_long($message.sync_node) != 0
then
    set_field("alert", "1");
end