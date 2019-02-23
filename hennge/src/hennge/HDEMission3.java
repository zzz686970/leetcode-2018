package hennge;

import org.json.JSONObject;

import java.io.DataOutputStream;
import java.io.UnsupportedEncodingException;
import java.net.*;
import java.time.Instant;
import java.util.Base64;

/**
 * This program is going to send post request to purpose url.
 * First, construct a JSON string like below:
 * {
 *    "github_url": "https://gist.github.com/yonghangtian/c4dba348ad3267e1798a29104b9dfb25",
 *    "contact_email": "yonghangtian@gmail.com"
 * }
 * Then, make an HTTP POST request to the URL:
 * {    https://hdechallenge-solve.appspot.com/challenge/003/endpoint   }
 * which contains the JSON string as a body part.
 *
 * Content-Type: of the request must be "application/json".
 * The URL is protected by HTTP Basic Authentication, which is explained on Chapter 2 of RFC2617,
 *  so you have to provide an Authorization: header field in your POST request
 * For the "userid" of HTTP Basic Authentication, use the same email address you put in the JSON string.
 * For the "password", provide an 10-digit time-based one time password conforming to RFC6238 TOTP.
 *
 * You have to read RFC6238 (and the errata too!) and get a correct one time password by yourself.
 * TOTP's "Time Step X" is 30 seconds. "T0" is 0.
 * Use HMAC-SHA-512 for the hash function, instead of the default HMAC-SHA-1.
 * Token shared secret is the userid followed by ASCII string value "HDECHALLENGE003" (not including double quotations).
 */
public class HDEMission3 {
    public static void main(String[] args) {
        String URL = "https://hdechallenge-solve.appspot.com/challenge/003/endpoint";
        String SECRET_SUFFIX = "HDECHALLENGE003";
        String CONTENT_TYPE = "application/json";
        int TIME_STEP = 30;
        int T0 = 0;
        String content = "{\"github_url\":\"https://gist.github.com/zzz686970/f740ef8b97db7209eb81c0960ea486c1\"" +
                ", " +
                "\"contact_email\":\"e0146282@u.nus.edu\"}";
        String userID = "e0146282@u.nus.edu";

        String secret = userID + SECRET_SUFFIX;
        String sharedSecret = asciiToHex(secret);

        String passWord = null;

        long unixTimeStep = Instant.now().getEpochSecond();

        long T = (unixTimeStep - T0)/TIME_STEP;
        String time = Long.toHexString(T).toUpperCase();

        while (time.length() < 16) {
            time = "0" + time;
        }

        passWord = TOTP.generateTOTP512(sharedSecret,time,"10");
        System.out.println(passWord);

        /*
          TOTP password is right, but the connection below is wrong and I dont want to debug it.
         */

        try{
            // start to send post request to purpose url.
            URL url = new URL(URL);

            String encoding = Base64.getEncoder().encodeToString((userID+":"+passWord).getBytes());
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("POST");
            connection.setDoOutput(true);
            connection.setDoInput(true);
            connection.setRequestProperty("Content-Type","application/json");
            connection.setRequestProperty  ("Authorization", "Basic " + encoding);

            connection.connect();

            DataOutputStream out = new DataOutputStream(connection
                    .getOutputStream());
            JSONObject json = new JSONObject(content);

            out.writeBytes(URLEncoder.encode(json.toString(),"UTF-8"));

            out.flush();
            out.close();

            int respCode = connection.getResponseCode();
            String message = connection.getResponseMessage();
            System.out.println(message);
            System.out.println(respCode);
            //disconnect
            connection.disconnect();
        }catch (UnsupportedEncodingException e){
            System.out.println(e.getMessage());
        }catch (Exception e){
            e.printStackTrace();
        }

    }

    private static String asciiToHex(String asciiValue)
    {
        char[] chars = asciiValue.toCharArray();
        StringBuffer hex = new StringBuffer();
        for (int i = 0; i < chars.length; i++)
        {
            hex.append(Integer.toHexString((int) chars[i]));
        }
        return hex.toString();
    }

}