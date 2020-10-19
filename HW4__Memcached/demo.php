<?php

$start_time = microtime(true);
$handle = opendir('uploads/');
$cache = 'cache/sample.cache.php';
if (file_exists(($cache)))
{
    include($cache);
    echo "Read Using Cache";
}
else
{
    $output = NULL;
    while (($file = readdir($handle)) != false)
    {
        $output .= $file . "<br />";
    }
    closedir($handle);

    echo $output;
    echo "Read Without using cache". "<br />";
    $fh = fopen($cache, 'w+') ;
    fwrite($fh, $output);
    fclose($fh);
}
echo "<br />";
$end_time = microtime(true);

$execution_time = ($end_time - $start_time);

echo " Execution time of script = ".$execution_time." sec";

?>