package com.example.pizzaorder;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.RadioButton;
import android.widget.TextView;
import android.widget.Toast;

import java.text.NumberFormat;
import java.util.Scanner;

import static android.view.View.GONE;

public class MainActivity extends AppCompatActivity {

    int pizzaNum = 1;
    int pizzaPrice = 4;
    double fullsum;

    String priceMessage, priceString;

    TextView textView_NumberOfPizzas, textView_FullSumForPizzas;
    RadioButton radiobutton_onlyPizza, radiobutton_pizzaWithAds;
    CheckBox checkbox_Mushrooms, checkbox_Corn, checkbox_Cucumbers;
    Button orderButton, button_Plus, button_Minus;
    EditText editText;
    LinearLayout linearLayout_pizzaWithAdds;


    @Override
    protected void onCreate(Bundle savedInstanceState) {


        super.onCreate(savedInstanceState);

        //We check and boost the app
        if (savedInstanceState != null) {
            pizzaNum = savedInstanceState.getInt("pizzaNumber");
            priceMessage = savedInstanceState.getString("priceMessage");
        }

        setContentView(R.layout.activity_main);

        //T E X T   V I E W S
        textView_NumberOfPizzas = findViewById(R.id.textView_NumberOfPizzas);
        textView_FullSumForPizzas = findViewById(R.id.textView_FullSumForPizzas);

        // R A D I O   B U T T O N S
        radiobutton_pizzaWithAds = findViewById(R.id.radiobutton_PizzaWithAdds);
        radiobutton_onlyPizza = findViewById(R.id.radiobutton_OnlyPizza);

        //C H E C K B O X E S
        checkbox_Mushrooms = findViewById(R.id.checkbox_Mushrooms);
        checkbox_Corn = findViewById(R.id.checkbox_Corn);
        checkbox_Cucumbers = findViewById(R.id.checkbox_Cucumbers);

        //O T H E R   B U T T O N S
        orderButton = findViewById(R.id.orderButton);
        button_Plus = findViewById(R.id.button_Plus);
        button_Minus = findViewById(R.id.button_Minus);

        //O T H E R   F U N C T I O N S   A N D   V A R I A B L E S
        editText = findViewById(R.id.editText);
        linearLayout_pizzaWithAdds = findViewById(R.id.linearLayout_pizzaWithAdds);
        linearLayout_pizzaWithAdds.setVisibility(View.GONE);
    }

    @Override
    public void onSaveInstanceState(Bundle savedInstanceState) {

        savedInstanceState.putString("pizzaMessage", priceMessage);
        savedInstanceState.putInt("pizzaNumber", pizzaNum);
        savedInstanceState.putInt("layPizzaWithAdds", linearLayout_pizzaWithAdds.getVisibility());

        super.onSaveInstanceState(savedInstanceState);
    }

    @Override
    protected void onRestoreInstanceState(Bundle savedInstanceState) {
        priceMessage = savedInstanceState.getString("pizzaMessage");
        pizzaNum = savedInstanceState.getInt("pizzaNumber");

        textView_NumberOfPizzas.setText(String.valueOf(pizzaNum));
        textView_FullSumForPizzas.setText(String.valueOf(priceMessage));

    }


    //THE MINIMUM OF THE PIZZAS
    public void button_Minus(View view) {
        //Checking the number of the pizza and remove one pizza from all
        pizzaNum--;
        if (pizzaNum <= 1) {
            pizzaNum = 1;
            Toast.makeText(this, "Не може да поръчате по-малко от 1 пица.", Toast.LENGTH_SHORT).show();
        }
        displayNumberOfPizzas(pizzaNum);
    }
    //---------------------------------//


    //THE MAXIMUM OF THE PIZZAS
    public void button_Plus(View view) {
        //Checking the number of the pizza and add one pizza from all
        pizzaNum++;
        if (pizzaNum >= 100) {
            pizzaNum = 100;
            Toast.makeText(this, "Не може да поръчате повече от 100 пици.", Toast.LENGTH_SHORT).show();
        }
        displayNumberOfPizzas(pizzaNum);
    }


    //BUTTON FOR THE ORDER
    public void orderButton(View view) {
        //Trim() ti izchstva praznite poleta (SPACE)
        String strNames = editText.getText().toString().trim();

        Intent intent = new Intent(Intent.ACTION_SENDTO);
        intent.setData(Uri.parse("mailto:"));
        intent.putExtra(Intent.EXTRA_EMAIL, new String[]{"dimitar@nexume.eu"});
        intent.putExtra(Intent.EXTRA_SUBJECT, "Just Pizza order for " + strNames);
        intent.putExtra(Intent.EXTRA_TEXT, priceMessage);

        fullsum = pizzaPrice * pizzaNum;
        displayNumberOfPizzas(pizzaNum);
        displayFullSumForPizzas(fullsum);

        priceString = String.valueOf(NumberFormat.getCurrencyInstance().format(pizzaPrice));

        priceMessage = "Обща стойност: " + fullsum + "\nБлагодаря Bи" + strNames + "!";
        displayMessage(priceMessage);

        if (intent.resolveActivity(getPackageManager()) != null) {
            startActivity(intent);

        }
    }


    //Showing text
    private void displayNumberOfPizzas(int number) {
        String numberStr = String.valueOf(number);
        textView_NumberOfPizzas.setText(numberStr);
    }


    //Showing Price
    private void displayFullSumForPizzas(double fullsum) {
        textView_FullSumForPizzas.setText(NumberFormat.getCurrencyInstance().format(fullsum));
    }

    //STRINGS MADE IN ONE
    private void displayMessage(String messege) {
        textView_FullSumForPizzas.setText(messege);
    }


    //Check which radio button was clicked
    public void onRadioButtonClicked(View view) {

        boolean checked = ((RadioButton) view).isChecked();

        switch (view.getId()) {

            //FirstButton ID
            case R.id.radiobutton_OnlyPizza:
                if (checked) {
                    linearLayout_pizzaWithAdds.setVisibility(View.GONE);

                    checkbox_Mushrooms.setChecked(false);
                    checkbox_Corn.setChecked(false);
                    checkbox_Cucumbers.setChecked(false);
                    break;
                }

                //SecondButton ID
            case R.id.radiobutton_PizzaWithAdds:
                if (checked) {
                    linearLayout_pizzaWithAdds.setVisibility(View.VISIBLE);
                    break;
                }
        }
    }


}
