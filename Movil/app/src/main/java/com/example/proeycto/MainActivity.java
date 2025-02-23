package com.example.proeycto;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import java.util.Locale;

public class MainActivity extends AppCompatActivity {

    private EditText editTextName;
    private Button buttonCapitalize;
    private TextView textViewResult;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize views
        editTextName = findViewById(R.id.editTextName);
        buttonCapitalize = findViewById(R.id.buttonCapitalize);
        textViewResult = findViewById(R.id.textViewResult);

        // Set click listener for the button
        buttonCapitalize.setOnClickListener(v -> capitalizeNames());
    }

    private void capitalizeNames() {
        String input = editTextName.getText().toString();

        // Check if input is empty
        if (input.trim().isEmpty()) {
            textViewResult.setText(getString(R.string.enter_name_error));
            return;
        }

        // Split the input into words
        String[] words = input.split("\\s+");
        StringBuilder result = new StringBuilder();

        // Capitalize each word
        for (int i = 0; i < words.length; i++) {
            if (!words[i].isEmpty()) {
                if (i > 0) {
                    result.append(" ");
                }
                String word = words[i].toLowerCase();
                result.append(Character.toUpperCase(word.charAt(0)))
                        .append(word.substring(1));
            }
        }

        // Show the result
        textViewResult.setText(result.toString());
    }
}