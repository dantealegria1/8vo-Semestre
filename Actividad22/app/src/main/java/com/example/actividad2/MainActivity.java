package com.example.actividad2;

package com.tudominio.miaplicacion;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.graphics.Color;

import com.example.actividad2.customviews.MiVistaPersonalizada;

public class MainActivity extends AppCompatActivity {
    private MiVistaPersonalizada miVistaPersonalizada;
    private Button btnAccion;
    private boolean modoAlternativo = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Inicializar vistas
        miVistaPersonalizada = findViewById(R.id.miVistaPersonalizada);
        btnAccion = findViewById(R.id.btnAccion);

        // Configurar listener del botón
        btnAccion.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (modoAlternativo) {
                    miVistaPersonalizada.setTitulo("Mi Vista Personalizada");
                    miVistaPersonalizada.setColorFondo(Color.parseColor("#E0E0E0"));
                } else {
                    miVistaPersonalizada.setTitulo("¡Modo Alternativo!");
                    miVistaPersonalizada.setColorFondo(Color.parseColor("#FFD700"));
                }
                modoAlternativo = !modoAlternativo;
            }
        });
    }
}