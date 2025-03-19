package com.example.math;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.example.mathlibrary.MathOperations;

public class MainActivity extends AppCompatActivity {

    private TextView resultText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Asegúrate de que el TextView esté correctamente inicializado
        resultText = findViewById(R.id.resultText);

        // Referencias a los botones
        Button btnSum = findViewById(R.id.btnSum);
        Button btnSubtract = findViewById(R.id.btnSubtract);
        Button btnMultiply = findViewById(R.id.btnMultiply);

        // Acción para el botón de suma
        btnSum.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Llamar a la operación de suma de la librería MathOperations
                int sum = MathOperations.sum(5, 3);
                resultText.setText("Resultado: " + sum); // Actualizar el TextView con el resultado
            }
        });

        // Acción para el botón de resta
        btnSubtract.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Llamar a la operación de resta de la librería MathOperations
                int subtract = MathOperations.subtract(5, 3);
                resultText.setText("Resultado: " + subtract); // Actualizar el TextView con el resultado
            }
        });

        // Acción para el botón de multiplicación
        btnMultiply.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Llamar a la operación de multiplicación de la librería MathOperations
                int multiply = MathOperations.multiply(5, 3);
                resultText.setText("Resultado: " + multiply); // Actualizar el TextView con el resultado
            }
        });
    }
}
