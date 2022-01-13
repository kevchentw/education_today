import React, { useState } from "react";
import axios from "axios";
import { IMostCitedPapers } from "../types/MostCitedPapers";
import {
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
  Button,
  Input,
  FormLabel,
  FormControl,
  Box,
  Stack,
} from "@chakra-ui/react";

export default function MostCitedPapers() {
  const [data, setData] = useState<IMostCitedPapers[]>([]);
  const [limit, setLimit] = useState(10);
  const [authorId, setAuthorId] = useState(2096520082);

  async function fetchData() {
    try {
      const response = await axios.get("/api/most-cited-papers", {
        params: { limit, authorId },
      });
      setData(response.data);
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div>
      <Box w="250px">
        <Stack spacing={3}>
          <FormControl>
            <FormLabel>Limit</FormLabel>
            <Input
              value={limit}
              type="number"
              onChange={(e) => setLimit(parseInt(e.target.value))}
            />
          </FormControl>
          <FormControl>
            <FormLabel>Author Id</FormLabel>
            <Input
              value={authorId}
              type="number"
              onChange={(e) => setAuthorId(parseInt(e.target.value))}
            />
          </FormControl>
          <Button colorScheme="blue" onClick={fetchData}>
            Search
          </Button>
        </Stack>
      </Box>

      <Table>
        <Thead>
          <Tr>
            <Th>Paper Id</Th>
            <Th>Paper Title</Th>
            <Th>Cited Count</Th>
          </Tr>
        </Thead>
        <Tbody>
          {data.map((x) => (
            <Tr>
              <Td>{x.PaperId}</Td>
              <Td>{x.PaperTitle}</Td>
              <Td>{x.CitedByCount}</Td>
            </Tr>
          ))}
        </Tbody>
      </Table>
    </div>
  );
}
