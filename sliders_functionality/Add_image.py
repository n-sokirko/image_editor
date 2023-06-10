def add_image_to_list(self):
    self.image_list.append(self.image_label.pixmap().copy())
    self.current_image_index+=1         
    self.count_label.setText(f"Total Images: {self.current_image_index}")
    self.Brightness.setValue(50)
    self.Contrast.setValue(50)
   
    self.Undo_butt.setEnabled(True)