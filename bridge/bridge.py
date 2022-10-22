bridge_safe = lambda b: not (' ' in b)

bridge = "###"
safe = bridge_safe(bridge)

print(f"The bridge is {'safe' if safe else 'not safe'}")