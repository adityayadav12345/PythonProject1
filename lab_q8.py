# ============================================================================
# 8. FILE OPERATIONS ASSERTIONS
# ============================================================================

import os
import tempfile


class TestFileOperations:

    def setup_method(self):
        """Setup a temporary directory for each test."""
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = os.path.join(self.temp_dir.name, "test_file.txt")
        self.binary_path = os.path.join(self.temp_dir.name, "test_file.bin")

    def teardown_method(self):
        """Clean up the temporary directory."""
        self.temp_dir.cleanup()

    def test_file_creation_and_deletion(self):
        """Test file creation and deletion."""
        # Create a new file
        with open(self.file_path, "w") as f:
            f.write("Hello, File Testing!")

        # Assert file is created
        assert os.path.exists(self.file_path)

        # Delete file and check
        os.remove(self.file_path)
        assert not os.path.exists(self.file_path)

    def test_file_read_write_permissions(self):
        """Test write and read operations."""
        sample_text = "Pytest file operation check."
        with open(self.file_path, "w") as f:
            f.write(sample_text)

        # Read file
        with open(self.file_path, "r") as f:
            content = f.read()

        # Assertions
        assert content == sample_text
        assert len(content) == len(sample_text)

    def test_file_content_validation(self):
        """Validate that file content matches expected format."""
        content = "Line1\nLine2\nLine3"
        with open(self.file_path, "w") as f:
            f.write(content)

        with open(self.file_path, "r") as f:
            lines = f.readlines()

        # Assertions
        assert len(lines) == 3
        assert lines[0].strip() == "Line1"
        assert all(line.startswith("Line") for line in lines)

    def test_binary_file_operations(self):
        """Test writing and reading binary data."""
        data = bytes([120, 3, 255, 10, 60])

        # Write binary file
        with open(self.binary_path, "wb") as f:
            f.write(data)

        # Read binary file
        with open(self.binary_path, "rb") as f:
            read_data = f.read()

        # Assertions
        assert read_data == data
        assert isinstance(read_data, bytes)
        assert len(read_data) == 5
