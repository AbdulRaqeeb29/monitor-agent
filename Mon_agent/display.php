<?php 
  $db = "monitor_agent"; //database name
  $dbuser = "root"; //database username
  $dbpassword = "root"; //database password
  $dbhost = "172.17.0.1"; //database host

  
  $link = mysqli_connect($dbhost, $dbuser, $dbpassword, $db);
  if(!$link) {
    die('could not connect:'.mysqli_connect_error());
  }

  

// Run MySQL query (if provided)
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $query = $_POST["query"];
    $result = $conn->query($query);
    if ($result === FALSE) {
        echo "Error executing query: " . $conn->error;
    } else {
        echo "<h2>Query Result</h2>";
        echo "<table border='1'>";
        // Display column headers
        echo "<tr>";
        while ($fieldinfo = $result->fetch_field()) {
            echo "<th>{$fieldinfo->name}</th>";
        }
        echo "</tr>";
        // Display query results
        while ($row = $result->fetch_assoc()) {
            echo "<tr>";
            foreach ($row as $value) {
                echo "<td>$value</td>";
            }
            echo "</tr>";
        }
        echo "</table>";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>MySQL Query Tool</title>
</head>
<body>
    <h1>MySQL Query Tool</h1>
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
        <label for="query">Enter your MySQL query:</label><br>
        <textarea name="query" rows="5" cols="50"></textarea><br>
        <input type="submit" value="Run Query">
    </form>
</body>
</html>
