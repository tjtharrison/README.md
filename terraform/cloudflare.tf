resource "cloudflare_record" "tjth_cv" {
  for_each = toset(local.github_pages_ip_addresses)
  zone_id  = sensitive(local.cloudflare_zone_id)
  name     = local.custom_subdomain
  value    = each.key
  type     = "A"
  ttl      = 3600
}
