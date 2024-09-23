import numpy as np
from transform import Transform3D

def solving():
    
    transform = Transform3D()
    
    # Initial point in frame {A}
    pA = np.array([2, 3, 5])
    
    # Translation vector from frame {A} to frame {B}
    tA_to_B = np.array([1, -1, 2])
    
    # Perform translation to obtain point in frame {B}
    pB = pA + tA_to_B
    
    # Rotation angle θ=45 degrees around the Z-axis
    theta = np.radians(45)  # Convert degrees to radians
    
    # Create rotation matrix for rotation around the Z-axis
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])
    
    # Perform rotation to obtain point in frame {C}
    pC = rotation_matrix @ pB
    
    return pC

# Example usage with pytest
def test_solving():
    expected_result = np.array([2 - np.sqrt(2), 3 + np.sqrt(2), 7])
    np.testing.assert_almost_equal(solving(), expected_result)
