<!DOCTYPE html>
<html><meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<title>What's my IP</title>
	<body>
		<div id="ip-lookup" class="tools">
			<?php if ($_SERVER["HTTP_X_FORWARDED_FOR"] != "") {
				$IP = $_SERVER["HTTP_X_FORWARDED_FOR"];
				$proxy = $_SERVER["REMOTE_ADDR"];
				$host = @gethostbyaddr($_SERVER["HTTP_X_FORWARDED_FOR"]);
			} else {
				$IP = $_SERVER["REMOTE_ADDR"];
				$host = @gethostbyaddr($_SERVER["REMOTE_ADDR"]);
			} ?>
			<p><?php echo $IP; ?></p>
		</div>
	</body>
</html>