<?php

echo '
<!DOCTYPE html>
<html>
<body>
    <form action="inc/auth.php" class="authform" method="POST" accept-charset="utf-8">
        <fieldset>
            <legend>Authentication</legend>
            <input type="text" id="username" name="username" value="" placeholder="Your username" />
            <input type="password" id="password" name="password" value="" placeholder="Your password" />
            <input type="submit" name="submit" value="Authenticate" />
            <div class="return_value" style="padding: 10px 0"></div>
        </fieldset>
    </form>
    <br>

    <a target="_blank" href="https://www.owasp.org/images/6/6b/PHPMagicTricks-TypeJuggling.pdf"> <b> Hint... </b> </a>



    <script src="http://challenge01.root-me.org/web-serveur/ch44/jquery-2.2.1.min.js" type="text/javascript">
    </script>
    <script type="text/javascript">
        $("document").ready(function(){
            $(".authform").submit(function(){
                $(".return_value").html("Running...");
                var data = {username: $("#username").val(), password: $("#password").val()};
                $.ajax({
                    type: "POST",
                    dataType: "json",
                    url: "inc/auth.php",
                    data: {auth : JSON.stringify({data})},
                    success: function(data) {
                        $(".return_value").html("Result: " + data["status"]);
                    }
                });
                return false;
            });
        });
    </script>

</html>
</body>
    ';

?>




