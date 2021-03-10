package com.example.grocerystore;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.Typeface;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    TextView textView_Grocery, textView_Store;
    Typeface grocery_store_typeface, button_typeface;
    Button button_Fruits, button_Vegetables, button_MixProducts, button_ViewData;
    String check;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //B U T T O N S
    button_Fruits = findViewById(R.id.button_Fruits) ;
    button_Vegetables = findViewById(R.id.button_Vegetables);
    button_MixProducts = findViewById(R.id.button_MixProducts);
    button_ViewData = findViewById(R.id.button_ViewData);
    button_ViewData.setVisibility(View.GONE);

        //T E X T S
    textView_Grocery = findViewById(R.id.textView_Grocery);
    textView_Store = findViewById(R.id.textView_Store);

        //S E T  T E X T S  F O N T
    grocery_store_typeface = Typeface.createFromAsset(getAssets(), "LuckiestGuy-Regular.ttf");
    button_typeface = Typeface.createFromAsset(getAssets(), "Lobster-Regular.ttf");
    textView_Grocery.setTypeface(grocery_store_typeface);
    textView_Store.setTypeface(grocery_store_typeface);
    button_Fruits.setTypeface(button_typeface);
    button_Vegetables.setTypeface(button_typeface);
    button_MixProducts.setTypeface(button_typeface);
    button_ViewData.setTypeface(button_typeface);


    Bundle extras = getIntent().getExtras();
    if(extras != null)
    {
        check = extras.getString("check");
        if(check != null && !check.isEmpty())
        {
            button_ViewData.setVisibility(View.VISIBLE);
        }
    }

    button_ViewData.setOnClickListener(new View.OnClickListener()
    {
        @Override
        public void onClick(View v)
        {
            Intent intentAdminLayout = new Intent(MainActivity.this,AdminDataActivity.class);
            startActivity(intentAdminLayout);
        }
    });

        //A C T I V I T Y   C H A N G E (--M a i n A c t i v i t y ===> F r u i t s A c t i v i t y --)
    button_Fruits.setOnClickListener(new View.OnClickListener()
    {
        @Override
        public void onClick(View v)
        {
            Intent intentFruits = new Intent(MainActivity.this, Fruits.class);
            startActivity(intentFruits);
        }
    });
        //A C T I V I T Y   C H A N G E (--M a i n A c t i v i t y ===> V e g e t a b l e s A c t i v i t y --)
    button_Vegetables.setOnClickListener(new View.OnClickListener()
    {
        @Override
        public void onClick(View v)
        {
            Intent intentVegetables = new Intent(MainActivity.this, Vegetables.class);
            startActivity(intentVegetables);
        }
    });
        //A C T I V I T Y   C H A N G E (--M a i n A c t i v i t y ===> M i x A c t i v i t y --)
    button_MixProducts.setOnClickListener(new View.OnClickListener()
    {
        @Override
        public void onClick(View v)
        {
            Intent intentMixProducts = new Intent(MainActivity.this, Mix_Products.class);
            startActivity(intentMixProducts);
        }
    });

    }
}
