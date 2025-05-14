# smCreativeToSurvival

Converts Creative Blueprints for Survival Mode

All this does is adding the `"type": 0` property to any `"childs"` element inside the JSON file.

---

## 🔧 How to Use It

1. Download: `creative_to_survival.py`

3. Run it via terminal or command line like this: *(point to the blueprint.json file)*

   ```bash
   python creative_to_survival.py "C:/...path_to_your_blueprint.../your_file_name.json"
   ```

4. It will output: `your_file_name.blueprint` in the same directory

5. Move/Copy the `.blueprint` file into the Survival `LocalBlueprints` Folder

6. Enable Dev-Commands and just use: **`/import your_file_name`**

---

## 📂 Common Folder Paths:

- **CREATIVE BLUEPRINTS:** `C:\Users\<USER>\AppData\Roaming\Axolot Games\Scrap Mechanic\User\<YOUR_USER_ID>\Blueprints\`

- **SURVIVAL BLUEPRINTS:** `...\SteamLibrary\steamapps\common\Scrap Mechanic\Survival\LocalBlueprints\`

---

## ⚠️ Important Notes

- The script doesn’t change the original blueprint.
- If the `"type"` property already exists, it will **not** overwrite it.
- It should work with most vanilla creations as long as the same pieces exist in survival. *(Not extensibly tested)*
