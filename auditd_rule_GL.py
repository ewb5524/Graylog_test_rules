rule "auditd_kv_ex_prefix"
when
    has_field("is_auditd")
then
    // extract all key-value from "message"
    // and prefix it with auditd_ 
    set_fields(
        fields:
            key_value(
                value: to_string($message.message)
                trim_value_chars: "\""
            ),
        prefix: "auditd_"
    )
end