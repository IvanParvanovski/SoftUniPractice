package com.example.grocerystore;

        import androidx.appcompat.app.AppCompatActivity;

        import android.content.ContentValues;
        import android.content.Intent;
        import android.database.sqlite.SQLiteDatabase;
        import android.graphics.Typeface;
        import android.os.Bundle;
        import android.view.View;
        import android.widget.Button;
        import android.widget.EditText;
        import android.widget.TextView;
        import android.widget.Toast;

public class Registration extends AppCompatActivity
{
    TextView textView_Registration;
    Typeface typeFace_registration;
    Button button_Register;
    EditText editText_Username, editText_Password, editText_Address, editText_PopulatedPlace;
    EditText editText_FirstName, editText_LastName, editText_Age;

    AdminDataBaseHelper adminDataBaseHelper;
    SQLiteDatabase database;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_registration);

        textView_Registration = findViewById(R.id.textView_Registration);
        typeFace_registration = Typeface.createFromAsset(getAssets(), "Lobster-Regular.ttf");
        textView_Registration.setTypeface(typeFace_registration);
        button_Register = findViewById(R.id.button_RegisterActReg);
        editText_Username = findViewById(R.id.editText_UsernameActReg);
        editText_Password = findViewById(R.id.editText_PasswordActReg);
        editText_Address = findViewById(R.id.editText_Address);
        editText_PopulatedPlace = findViewById(R.id.editText_PopulatedPlace);
        editText_FirstName = findViewById(R.id.editText_FirstName);
        editText_LastName = findViewById(R.id.editText_LastName);
        editText_Age = findViewById(R.id.editText_Age);

        adminDataBaseHelper = new AdminDataBaseHelper(this);
        database = adminDataBaseHelper.getWritableDatabase();


        AddData();

    }

    public void AddData(){

        button_Register.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View v)
            {
                if(editText_Username.length() >= 3 && editText_Password.length() >= 3 && editText_Address.length() >= 5 && editText_FirstName.length() >= 3 && editText_PopulatedPlace.length() >= 3 && editText_LastName.length() >= 3 && editText_Age.length() != 0){

                    ContentValues values = new ContentValues();
                    values.put(AdminDataBaseHelper.Column_2, editText_Username.getText().toString().trim());
                    values.put(AdminDataBaseHelper.Column_3, editText_Password.getText().toString().trim());
                    values.put(AdminDataBaseHelper.Column_4, editText_Address.getText().toString().trim());
                    values.put(AdminDataBaseHelper.Column_5, editText_PopulatedPlace.getText().toString().trim());
                    values.put(AdminDataBaseHelper.Column_6, editText_FirstName.getText().toString().trim());
                    values.put(AdminDataBaseHelper.Column_7 ,editText_LastName.getText().toString().trim());
                    values.put(AdminDataBaseHelper.Column_8, editText_Age.getText().toString().trim());
                    database.insert(AdminDataBaseHelper.TABLE_NAME, null, values);

                        Intent intentChange = new Intent(Registration.this, MainActivity.class);
                        startActivity(intentChange);


                }else
                    {
                    Toast.makeText(Registration.this,"Data not Inserted", Toast.LENGTH_SHORT).show();
                    }

            }
        });

    }

    protected void onDestroy()
    {
        database.close();
        adminDataBaseHelper.close();
        super.onDestroy();
    }
}
