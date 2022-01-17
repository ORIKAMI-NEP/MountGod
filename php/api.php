<?php
header('Content-Type: application/json; charset=UTF-8');
$arr["status"] = "yes";
print json_encode($arr, JSON_PRETTY_PRINT);
