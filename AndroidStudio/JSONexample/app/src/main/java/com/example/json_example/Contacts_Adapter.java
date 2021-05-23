package com.example.json_example;

import android.content.Context;
import android.provider.ContactsContract;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import androidx.annotation.NonNull;

import java.util.List;


public class Contacts_Adapter extends ArrayAdapter<Contacts_Model>
{

    public Contacts_Adapter(Context context, List<Contacts_Model> contacts)
    {
        super(context, 0, contacts);
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent)
    {
        View list_ItemView = convertView;
        if(list_ItemView == null)
        {
            list_ItemView = LayoutInflater.from(getContext()).inflate(R.layout.list_item, parent, false);
        }

        Contacts_Model currentInfo = getItem(position);

        TextView nameView = list_ItemView.findViewById(R.id.name);
        nameView.setText(currentInfo.getmName());

        TextView emailView = list_ItemView.findViewById(R.id.name);
        nameView.setText(currentInfo.getmEmail());

        TextView dateView = list_ItemView.findViewById(R.id.name);
        nameView.setText(currentInfo.getmMobile());

        return list_ItemView;
    }

}


