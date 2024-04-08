<?php

class Methode {

    public bool $Errormanagement = false;
    public bool $journal = false;

    function get($url) {
        
        // init
        $ch = curl_init($url);
        
        // FR: Configuration de la requête cURL pour GET
        // EN: Configuring the cURL request for GET
        curl_setopt($ch, CURLOPT_HTTPGET, true);
        $ch = $this->configureCurl($ch);
        
        // Execution
        $reponse = curl_exec($ch);
        
        // FR: Gestion des erreurs
        // EN: Error management
        if ($reponse === false) {
            echo "ERREUR GET";
            $retour = false;
        } else {
            $retour = $reponse;
        }
        
        // FR: Fermeture de la ressource cURL
        // EN: Closing the cURL resource
        curl_close($ch);

        return $retour;

    }
    
    function post($url, $data) {

        // init
        $ch = curl_init($url);
        
        // Configuration de la requête cURL pour POST
        // EN: Configuring the cURL request for POST
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
        $ch = $this->configureCurl($ch);
        
        // Execution
        $reponse = curl_exec($ch);
        
        // FR: Gestion des erreurs
        // EN: Error management
        if ($reponse === false) {
            echo "ERREUR POST";
            $retour = false;
        } else {
            $retour = $reponse;
        }
        
        // FR: Fermeture de la ressource cURL
        // EN: Closing the cURL resource
        curl_close($ch);

        return $retour;
    }
    
    

    function delete($url) {
    
        // init
        $ch = curl_init($url);
        
        // Configuration de la requête cURL pour DELETE
        // EN: Configuring the cURL request for DELETE
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "DELETE");
        $ch = $this->configureCurl($ch);
        
        // Execution
        $reponse = curl_exec($ch);
        
        // FR: Gestion des erreurs
        // EN: Error management
        if ($reponse === false) {
            echo "ERREUR DELETE";
            $retour = false;
        } else {
            $retour = $reponse;
        }
        
        // FR: Fermeture de la ressource cURL
        // EN: Closing the cURL resource
        curl_close($ch);

        return $retour;

    }

    function put($url, $data) {
      
        // init
        $ch = curl_init($url);

        // Configuration de la requête cURL pour PUT
        // EN: Configuring the cURL request for PUT
        curl_setopt($ch, CURLOPT_URL, $url);
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PUT');
        curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
        $ch = $this->configureCurl($ch);
      
        // Execution
        $reponse = curl_exec($ch);
        
        // FR: Gestion des erreurs
        // EN: Error management
        if ($reponse === false) {
            echo "ERREUR PUT";
            $retour = false;
        } else {
            $retour = $reponse;
        }
        
        // FR: Fermeture de la ressource cURL
        // EN: Closing the cURL resource
        curl_close($ch);

        return $retour;
      }

      function configureCurl($ch) {
        curl_setopt($ch, CURLOPT_HEADER, false);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 20);
        curl_setopt($ch, CURLOPT_TIMEOUT, 30);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($ch, CURLOPT_USERAGENT, 'BOT_VEILLE/3.0');
        return $ch;
      }
    
}


?>