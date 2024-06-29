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

function DisorderSelector({
  disorders,
  selectedDisorders,
  handleDisorderChange,
  handleRemoveDisorder,
}) {
  return (
    <Box mt={2}>
      <TextField
        label="Select a disorder"
        select
        onChange={handleDisorderChange}
        fullWidth
        margin="normal"
        placeholder="Select a disorder"
      >
        {disorders.map((disorder) => (
          <MenuItem key={disorder} value={disorder}>
            {disorder}
          </MenuItem>
        ))}
      </TextField>
      <List>
        {selectedDisorders.map((disorder) => (
          <ListItem key={disorder}>
            <ListItemText primary={disorder} />
            <ListItemSecondaryAction>
              <IconButton
                edge="end"
                color="secondary"
                onClick={() => handleRemoveDisorder(disorder)}
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

export default DisorderSelector;
