package com.example.grocerystore;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.Typeface;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class LoginAndRegisterActivity extends AppCompatActivity
{

    Button button_Login, button_Register;
    TextView textView_StartMenu;
    Typeface start_menu, button_menu;
    EditText editText_Username, editText_Password;
    AdminDataBaseHelper adminDataBaseHelper;
    String check;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login_and_register);

        textView_StartMenu = findViewById(R.id.textView_StartMenu);
        editText_Password = findViewById(R.id.editText_Password);
        editText_Username = findViewById(R.id.editText_Username);
        button_Register = findViewById(R.id.button_Register);
        button_Login = findViewById(R.id.button_Login);

        start_menu = Typeface.createFromAsset(getAssets(), "Lobster-Regular.ttf");
        button_menu = Typeface.createFromAsset(getAssets(), "PassionOne-Bold.ttf");
        textView_StartMenu.setTypeface(start_menu);
        button_Register.setTypeface(button_menu);
        button_Login.setTypeface(button_menu);

        adminDataBaseHelper = new AdminDataBaseHelper(this);

        button_Register.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                Intent intentRegister = new Intent(LoginAndRegisterActivity.this, Registration.class);
                startActivity(intentRegister);
            }
        });
        button_Login.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {

                String userUserNameInput = editText_Username.getText().toString().trim();
                String userPasswordInput = editText_Password.getText().toString().trim();

                if (userUserNameInput.equalsIgnoreCase("Admin") && userPasswordInput.equalsIgnoreCase("Admin") )
                {
                    Intent intentChange = new Intent(LoginAndRegisterActivity.this, MainActivity.class);
                    check = "admin";
                    intentChange.putExtra("check", check);
                    startActivity(intentChange);
                } else {
                     check = "";
                     Toast.makeText(LoginAndRegisterActivity.this,"The password or the username is incorrect.", Toast.LENGTH_LONG).show();
                    }
            }
        });

    }

}
