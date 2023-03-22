<?php
$target = $_REQUEST[ 'ip' ];
$perdu = 100;

if( isset( $_POST[ 'submit' ]) && $_POST[ 'ip' ] != "" ) {
	// Get input
	$target = $_REQUEST[ 'ip' ];

	// Determine OS and execute the ping command.
	if( stristr( php_uname( 's' ), 'Windows NT' ) ) {
		// Windows
		$cmd = shell_exec( 'ping  ' . $target );
	}
	else {
		// *nix
		$cmd = shell_exec( 'ping  -c 4 ' . $target );
	}

	$posPerte = strpos($cmd, "perte");
	$posPourcent = strpos($cmd, "%");

	$perdu = substr($cmd, $posPerte+6, $posPourcent-$posPerte-6);

	// Feedback for the end user
	// echo "<pre>{$cmd}</pre>";
}
?>

<!doctype html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="../dist/output.css" rel="stylesheet">
</head>
<body>
    <div class="bg-white">
        <div class="mx-auto max-w-7xl py-24 sm:px-6 sm:py-32 lg:px-8">
          <div class="relative isolate overflow-hidden px-6 pt-16 shadow-2xl sm:rounded-3xl sm:px-16 md:pt-24 lg:flex lg:gap-x-20 lg:px-24 lg:pt-0 bg-gradient-to-tl from-sky-200 via-orange-400 to-pink-600">
            <div class="mx-auto max-w-md text-center lg:mx-0 lg:flex-auto lg:py-32 lg:text-left">
              <h2 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">My device is online ?</h2>
              <p class="mt-6 text-lg leading-8 text-white">Enter the ip of your device and know if it's online !</p>
              <div class="mt-10 flex items-center justify-center gap-x-6 lg:justify-start">
              </div>
            </div>
            <div class="relative mt-16 h-80 lg:mt-8 flex items-center">
                    <div class="flex items-center">
						<div class="mr-4">
                        	<h1 class="block text-1xl font-bold leading-6 text-white">IP Address : <?php echo $target; ?></h1>
						<?php if ($perdu == 0) { ?>
								<h1 class="block text-1xl font-bold leading-6 text-white">Status : Online</h1>
							</div>
							<img class="scale-150" src="../res/IcBaselineCheckCircle.svg" alt="check">
						<?php } else { ?>
								<h1 class="block text-1xl font-bold leading-6 text-white">Status : Offline</h1>
							</div>
							<img class="scale-150" src="../res/IcBaselineError.svg" alt="error" fill="red">
						<?php } ?>
					</div>
            </div>
          </div>
        </div>
      </div>
      
</body>
</html>
