package com.example.proyecto;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    private EditText editTextName;
    private Button buttonCapitalize;
    private TextView textViewOriginal;
    private TextView textViewCapitalized;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Inicializar vistas
        editTextName = findViewById(R.id.editTextName);
        buttonCapitalize = findViewById(R.id.buttonCapitalize);
        textViewOriginal = findViewById(R.id.textViewOriginal);
        textViewCapitalized = findViewById(R.id.textViewCapitalized);

        // Configurar el click listener del botón
        buttonCapitalize.setOnClickListener(v -> capitalizeText());
    }

    private void capitalizeText() {
        String input = editTextName.getText().toString();
        if (!input.isEmpty()) {
            // Mostrar el texto original
            textViewOriginal.setText(input);

            // Dividir el texto en palabras
            String[] words = input.toLowerCase().split("\\s");
            StringBuilder result = new StringBuilder();

            // Capitalizar cada palabra
            for (String word : words) {
                if (word.length() > 0) {
                    result.append(Character.toUpperCase(word.charAt(0)))
                            .append(word.substring(1))
                            .append(" ");
                }
            }

            // Mostrar el texto capitalizado
            textViewCapitalized.setText(result.toString().trim());
            editTextName.setText(""); // Limpiar el campo de entrada
        }
    }
}