rule "anonymize_ip"
when
    has_field("ip_address")
then 
    let ip_addr = to_string($message.ip_address);
    let hash = sha256(ip_addr);
    set_field("ip_address", hash);
end

