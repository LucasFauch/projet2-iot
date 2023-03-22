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
                <form name="ping" action="ping.php" method="post">
                    <div>
                        <label for="ip" class="block text-1xl font-bold leading-6 text-white">IP Address :</label>
                        <div class="relative mt-2 rounded-md shadow-sm">
                          <input type="text" name="ip" id="command" class="block w-full rounded-md border-0 py-1.5 pl-1 text-gray-900 ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 sm:text-sm sm:leading-6" placeholder="127.0.0.0">
                        </div>
                    </div>
                    <div class="my-2.5">
                        <input type="submit" name="submit" value="Submit" class="bg-sky-200 hover:bg-sky-400 text-white font-bold py-2 px-4 border-b-4 border-bg-sky-200 hover:border-bg-sky-300 rounded">
                    </div>
                </form>
            </div>
          </div>
        </div>
      </div>
      
</body>
</html>