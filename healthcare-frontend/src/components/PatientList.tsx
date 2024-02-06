import React, {useState, useEffect} from "react";
import {request, gql} from 'graphql-request';

interface Patient {
    id: number;
    name: string;
    age: number;
    gender: string;
}

const PATIENTS_QUERY = gql`
  query {
    allPatients {
      id
      name
      age
      gender
    }
  }
`;

const PatientList: React.FC = () => {
    const [patients, setPatients] = useState<Patient[]>([]);
  
    useEffect(() => {
      const fetchData = async () => {
        try {
            const data: { allPatients: Patient[] } = await request('http://127.0.0.1:8000/graphql', PATIENTS_QUERY);          setPatients(data.allPatients);
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      };
  
      fetchData();
    }, []);

    return (
        <div>
          <h2>Patient List</h2>
          <ul>
            {patients.map((patient) => (
              <li key={patient.id}>
                {patient.name} - {patient.age} - {patient.gender}
              </li>
            ))}
          </ul>
        </div>
      );
    };
    
    export default PatientList;