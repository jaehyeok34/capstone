import React from "react";
import { styled } from '@mui/material/styles';
import Button from '@mui/material/Button';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import { useState } from "react";

const VisuallyHiddenInput = styled('input')({
    clip: 'rect(0 0 0 0)',
    clipPath: 'inset(100%)',
    height: 1,
    overflow: 'hidden',
    position: 'absolute',
    bottom: 0,
    left: 0,
    whiteSpace: 'nowrap',
    width: 1,
  });

const InputData = () => {
    const [file, setFile] = useState(null);
    const [option, setOption] = useState("");
    const [message, setMessage] = useState(""); 

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleOptionChange = (e) => {
        setOption(e.target.value);
    };

    const options = [ "option1", "option2", "option3" ];

    const handleSubmit = async (e) => {
        e.preventDefault();
        if(!file || !option) {
            setMessage("Please select a file and an option.");
            return;
        }
        const formData = new FormData();
        formData.append("file", file);
        formData.append("option", option);

        try {
            const response = await fetch("http://localhost:8080/upload", {
                method: "POST",
                body: formData,   
            });

            const result = await response.json();
            setMessage(result.message);
            console.log(result);
        } catch (error) {
            console.error("Error:", error);
            setMessage("Error occurred. Please try again later.");
        }    
    };


    return (
        <form onSubmit={handleSubmit}>
            <Button
                component="label"
                variant="contained"
                startIcon={<CloudUploadIcon />}
            >
                Upload File
                <VisuallyHiddenInput
                    type="file"
                    onChange={handleFileChange}
                    multiple
                />
            </Button>
            <select value={option} onChange={handleOptionChange}>
                <option value="">Select an option</option>
                {options.map((opt, index) => (
                    <option key={index} value={opt}>
                        {opt === "option1" ? "마스킹처리" : opt === "option2" ? "삭제처리" : "통계처리"}
                    </option>
                ))}
            </select>
            <button type="submit">Submit</button>

            {message && <p>{message}</p>}
        </form>
    );
};


export default InputData;
// </select></form></select>

