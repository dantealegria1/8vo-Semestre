package com.example.actividad1;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

import java.util.List;

public class CustomAdapter extends ArrayAdapter<Item> {
    private Context context;
    private List<Item> itemList;

    // ViewHolder pattern para mejorar el rendimiento
    static class ViewHolder {
        TextView txtTitle;
        TextView txtDescription;
    }

    public CustomAdapter(Context context, List<Item> items) {
        super(context, R.layout.list_item, items);
        this.context = context;
        this.itemList = items;
    }

    @NonNull

    public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
        ViewHolder viewHolder;

        // Comprueba si la vista está siendo reusada
        if (convertView == null) {
            // Si no se está reusando, inflar el layout y crear un nuevo ViewHolder
            LayoutInflater inflater = LayoutInflater.from(context);
            convertView = inflater.inflate(R.layout.list_item, parent, false);

            // Inicializar el ViewHolder
            viewHolder = new ViewHolder();
            viewHolder.txtTitle = convertView.findViewById(R.id.txt_title);
            viewHolder.txtDescription = convertView.findViewById(R.id.txt_description);

            // Guardar el ViewHolder en la vista para reutilizarlo
            convertView.setTag(viewHolder);
        } else {
            // Si la vista está siendo reusada, recuperar el ViewHolder guardado
            viewHolder = (ViewHolder) convertView.getTag();
        }

        // Obtener el item actual y configurar los views
        Item currentItem = itemList.get(position);
        viewHolder.txtTitle.setText(currentItem.getTitle());
        viewHolder.txtDescription.setText(currentItem.getDescription());

        return convertView;
    }
}
