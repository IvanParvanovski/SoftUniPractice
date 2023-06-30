package com.example.;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.ContentValues;
import android.content.Intent;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

public class MainActivity extends AppCompatActivity {

    private SQLiteDatabase database;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Отваряне на базата данни
        database = openOrCreateDatabase("barcode_info.db", MODE_PRIVATE, null);
        database.execSQL("CREATE TABLE IF NOT EXISTS products (code TEXT PRIMARY KEY, name TEXT, ingredients TEXT)");

        // Намиране на елементите във layout-a
        EditText barcodeEditText = findViewById(R.id.my_edit_text);
        Button searchButton = findViewById(R.id.my_button);
        TextView productNameTextView = findViewById(R.id.my_text_view);
        TextView ingredientsTextView = findViewById(R.id.my_text_view_second);

        // Настройка на бутона за търсене
        searchButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String barcode = barcodeEditText.getText().toString();

                // Търсене в базата данни
                Product product = getProductFromDatabase(barcode);
                if (product != null) {
                    // Ако продуктът е намерен в базата, показваме информацията оттам
                    productNameTextView.setText(product.product_name);
                    ingredientsTextView.setText(product.ingredients_text);
                } else {
                    // Ако продуктът не е намерен в базата, правим заявка към API-то
                    String url = "https://world.openfoodfacts.org/api/v0/product/" + barcode + ".json";
                    JsonObjectRequest request = new JsonObjectRequest(Request.Method.GET, url, null,
                            new Response.Listener<JSONObject>() {
                                @Override
                                public void onResponse(JSONObject response) {
                                    try {
                                        // Извличане на информацията за продукта от JSON обекта
                                        JSONObject productObject = response.getJSONObject("product");
                                        String productName = productObject.getString("product_name");
                                        String ingredients = productObject.getString("ingredients_text");

                                        // Записване на информацията в базата данни
                                        ContentValues values = new ContentValues();
                                        values.put("code", barcode);
                                        values.put("name", productName);
                                        values.put("ingredients", ingredients);
                                        database.insert("products", null, values);

                                        // Показване на информацията
                                        productNameTextView.setText(productName);
                                        ingredientsTextView.setText(ingredients);
                                    } catch (JSONException e) {
                                        e.printStackTrace();
                                        Toast.makeText(MainActivity.this, "Грешка при обработка на отговора от API-то.", Toast.LENGTH_SHORT).show();
                                    }
                                }
                            },
                            new Response.ErrorListener() {
                                @Override
                                public void onErrorResponse(VolleyError error) {
                                    Toast.makeText(MainActivity.this, "Грешка при заявка до API-то.", Toast.LENGTH_SHORT).show();
                                }
                            });
                    Volley.newRequestQueue(MainActivity.this).add(request);
                }
            }
        });
    }

    private Product getProductFromDatabase(String barcode) {
        String[] columns = {"code", "name", "ingredients"};
        String selection = "code=?";
        String[] selectionArgs = {barcode};
        Cursor cursor = database.query("products", columns, selection, selectionArgs, null, null, null);
        if (cursor.moveToFirst()) {
            @SuppressLint("Range") String name = cursor.getString(cursor.getColumnIndex("name"));
            @SuppressLint("Range") String ingredients = cursor.getString(cursor.getColumnIndex("ingredients"));
            return new Product(barcode, name, ingredients);
        }
        return null;
    }


    public class Product {
        public String code;
        public String product_name;
        public String ingredients_text;

        public Product(String code, String product_name, String ingredients_text) {
            this.code = code;
            this.product_name = product_name;
            this.ingredients_text = ingredients_text;
        }
    }

}
