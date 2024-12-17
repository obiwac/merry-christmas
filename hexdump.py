html = ""

with open("boot.bin", "rb") as f:
	data = f.read()

for i, b in enumerate(data):
	if i % 32 == 0 and i != 0:
		html += "<br>"

	html += f"{b:02X} "

with open("hexdump.html", "w") as f:
	f.write(f"""
		<!DOCTYPE html>
			<html>
			<head>
				<title>Hexdump</title>
			</head>
			<body>
				<pre style="font-weight: bold; font-size: small; line-height: 170%">
{html}
				</pre>
			</body>
		</html>
	""")
