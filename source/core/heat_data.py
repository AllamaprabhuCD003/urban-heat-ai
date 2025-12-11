"""Heat data loading and preprocessing module.

This module provides utilities for loading, validating, and normalizing
heat-related data from various sources.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from typing import Optional, Tuple
import logging

logger = logging.getLogger(__name__)


class HeatDataLoader:
    """Load and preprocess urban heat data.
    
    Attributes:
        data_path: Path to the data directory.
        data: Loaded dataframe.
    """
    
    def __init__(self, data_path: str) -> None:
        """Initialize the HeatDataLoader.
        
        Args:
            data_path: Path to the data directory or file.
        """
        self.data_path = Path(data_path)
        self.data: Optional[pd.DataFrame] = None
        logger.info(f"Initialized HeatDataLoader with path: {data_path}")
    
    def load_data(self) -> pd.DataFrame:
        """Load heat data from CSV files.
        
        Returns:
            Loaded dataframe with heat data.
            
        Raises:
            FileNotFoundError: If data file not found.
        """
        try:
            if self.data_path.is_file():
                self.data = pd.read_csv(self.data_path)
            else:
                # Load multiple CSV files if directory provided
                csv_files = list(self.data_path.glob('*.csv'))
                if not csv_files:
                    raise FileNotFoundError(f"No CSV files found in {self.data_path}")
                self.data = pd.concat([pd.read_csv(f) for f in csv_files], ignore_index=True)
            
            logger.info(f"Loaded data with shape: {self.data.shape}")
            return self.data
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def validate_data(self) -> bool:
        """Validate the loaded data.
        
        Returns:
            True if data is valid, False otherwise.
        """
        if self.data is None:
            logger.warning("No data loaded for validation")
            return False
        
        required_columns = ['temperature', 'humidity', 'latitude', 'longitude']
        missing_cols = [col for col in required_columns if col not in self.data.columns]
        
        if missing_cols:
            logger.error(f"Missing required columns: {missing_cols}")
            return False
        
        if self.data.empty:
            logger.error("Data is empty")
            return False
        
        logger.info("Data validation passed")
        return True
    
    def normalize_data(self) -> pd.DataFrame:
        """Normalize numerical columns to [0, 1] range.
        
        Returns:
            Normalized dataframe.
        """
        if self.data is None:
            raise ValueError("No data loaded. Call load_data() first.")
        
        normalized = self.data.copy()
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols:
            min_val = self.data[col].min()
            max_val = self.data[col].max()
            if max_val > min_val:
                normalized[col] = (self.data[col] - min_val) / (max_val - min_val)
        
        logger.info("Data normalization completed")
        return normalized
