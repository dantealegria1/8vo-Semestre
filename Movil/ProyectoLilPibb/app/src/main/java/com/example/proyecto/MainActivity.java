package com.example.proyecto;
import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    private EditText editTextName;
    private TextView textViewOriginal;
    private TextView textViewCapitalized;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Inicializar vistas
        editTextName = findViewById(R.id.editTextName);

        textViewCapitalized = findViewById(R.id.textViewCapitalized);

        // Agregar un TextWatcher para capitalizar en tiempo real
        editTextName.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {}

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                updateCapitalizedText(s.toString());
            }

            @Override
            public void afterTextChanged(Editable s) {}
        });
    }

    private void updateCapitalizedText(String input) {
        if (!input.trim().isEmpty()) {

            textViewCapitalized.setText("🟢 Capitalizado: " + capitalizeWords(input));
        } else {

            textViewCapitalized.setText("");
        }
    }

    public static String capitalizeWords(String text) {
        String[] words = text.toLowerCase().trim().replaceAll("\\s+", " ").split(" ");
        StringBuilder result = new StringBuilder();

        for (String word : words) {
            if (!word.isEmpty()) {
                result.append(Character.toUpperCase(word.charAt(0)))
                        .append(word.substring(1))
                        .append(" ");
            }
        }
        return result.toString().trim();
    }
}