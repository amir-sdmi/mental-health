import {
  Box,
  TextField,
  MenuItem,
  List,
  ListItem,
  ListItemText,
  ListItemSecondaryAction,
  IconButton,
} from "@mui/material";
import CloseIcon from "@mui/icons-material/Close";

function HappinessSelector({
  happinesses,
  selectedHappiness,
  handleHappinessChange,
  handleRemoveHappiness,
}) {
  return (
    <Box mt={2}>
      <TextField
        label="Select a happiness"
        select
        onChange={handleHappinessChange}
        fullWidth
        margin="normal"
      >
        {happinesses.map((happiness) => (
          <MenuItem key={happiness} value={happiness}>
            {happiness}
          </MenuItem>
        ))}
      </TextField>
      <List>
        {selectedHappiness.map((happiness) => (
          <ListItem key={happiness}>
            <ListItemText primary={happiness} />
            <ListItemSecondaryAction>
              <IconButton
                edge="end"
                color="secondary"
                onClick={() => handleRemoveHappiness(happiness)}
              >
                <CloseIcon />
              </IconButton>
            </ListItemSecondaryAction>
          </ListItem>
        ))}
      </List>
    </Box>
  );
}

export default HappinessSelector;
