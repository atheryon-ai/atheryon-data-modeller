package ai.atheryon.cdmservice;

import org.springframework.web.bind.annotation.*;
import org.isda.cdm.model.Trade;

@RestController
@RequestMapping("/cdm")
public class CdmController {
    @GetMapping("/ping")
    public String ping() {
        return "CDM service is running!";
    }

    @PostMapping("/transform")
    public Trade transform(@RequestBody String fpml) {
        // TODO: parse FpML and map to CDM Trade object
        return new Trade();
    }
}
